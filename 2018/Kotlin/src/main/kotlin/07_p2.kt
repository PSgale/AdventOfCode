import java.util.*
import kotlin.math.max

private val REGEX = Regex("Step (.+) must be finished before step (.+) can begin.")

fun main() {
    val inputs = "src/main/inputs/"

    var timeDelay = 0
    var numWorkers = 2
    var totalTime = getInstructionsOrder(inputs + "07-instructions_list-t1.txt", numWorkers, timeDelay, true)
    println("It would take $totalTime seconds")


    timeDelay = 60
    numWorkers = 5
    totalTime = getInstructionsOrder(inputs + "07-instructions_list-p1.txt", numWorkers, timeDelay, true)
    println("It would take $totalTime seconds")

}

private fun getInstructionsOrder(fileName: String, numWorkers: Int, timeDelay: Int, isDebug: Boolean = false): Int {
    val lines = readFileLines(fileName)
    val instructions  = getInstructions(lines, isDebug)

    if (isDebug)
        println(instructions)

    val (executionOrder, totalTime) = getExecutionOrder(instructions, numWorkers, timeDelay, isDebug)

    if (isDebug)
        println("It would take $totalTime seconds for $numWorkers workers to complete these steps in order $executionOrder")

    return totalTime
}

private fun getExecutionOrder(instructions: MutableMap<String, MutableList<String>>, numWorkers: Int, timeDelay: Int, isDebug : Boolean = false): Pair<String, Int>{
    val availableSteps = PriorityQueue<String>()
    val visitedSteps = ArrayDeque<String>()
    val workerQueue = PriorityQueue<WorkItem>{workItem1, workItem2 -> workItem1.time - workItem2.time}

    // WorkItem with empty name = dummy
    for (worker in 0 until numWorkers) workerQueue.add(WorkItem("", 0))

    var executionOrder = ""
    var totalTime = 0

    // Check instructions without dependencies
    addAvailableStep(instructions, availableSteps, visitedSteps, isDebug)

    // Process instructions in order
    while (availableSteps.isNotEmpty() || workerQueue.any{ it.name != "" } ) {
        // if available items and free worker
        if (availableSteps.isNotEmpty() && workerQueue.minOf{it.time} == 0)
        {
            assignInstruction(availableSteps, workerQueue, timeDelay, isDebug)
        }

        // if no available items and all worker are busy
        if(availableSteps.isEmpty() || workerQueue.minOf{it.time} > 0)
        {
            val (doneInstruction, executionTime) = executeInstruction(instructions, workerQueue, isDebug)
            executionOrder += doneInstruction
            totalTime += executionTime

            // Check instructions without dependencies
            addAvailableStep(instructions, availableSteps, visitedSteps, isDebug)
        }

        if (isDebug) {
            println("Available Steps: $availableSteps")
        }

        if (isDebug) {
            println("Workers: $workerQueue")
        }
    }

    return Pair(executionOrder, totalTime)
}
fun timeToProcess(workItem: String, timeDelay: Int) = timeDelay + 1 + workItem[0].code - 'A'.code

private fun addAvailableStep(
    instructions: MutableMap<String, MutableList<String>>,
    availableSteps: PriorityQueue<String>,
    visitedSteps: ArrayDeque<String>,
    isDebug: Boolean = false) {

    for ((nextStep, _) in instructions.filter { (k, v) -> v.isEmpty() && k !in visitedSteps }) {
        availableSteps.add(nextStep)
        visitedSteps.addFirst(nextStep)

        if (isDebug) {
            println("Next available step: $nextStep")
        }
    }
}

private fun executeInstruction(
    instructions: MutableMap<String, MutableList<String>>,
    workerQueue: PriorityQueue<WorkItem>,
    isDebug: Boolean = false): Pair<String?, Int>{

    val activeWorkers = workerQueue.filter { it.name != "" }.sortedBy { it.time }
    val doneWorker = activeWorkers[0]

    workerQueue.remove(doneWorker)
    workerQueue.add(WorkItem("", 0))

    val executionTime = doneWorker.time
    val doneInstruction = doneWorker.name

    // update time for the rest Workers
    for (item in workerQueue) item.time = max(0, item.time - executionTime)

    // remove dependencies for completed Step
    instructions.values.filter { it.contains(doneInstruction) }.forEach { it.remove(doneInstruction) }

    if (isDebug) {
        println("Done step: $doneInstruction")
    }
    return Pair(doneInstruction, executionTime);
}

private fun assignInstruction(
    availableSteps: PriorityQueue<String>,
    workerQueue: PriorityQueue<WorkItem>,
    timeDelay: Int,
    isDebug: Boolean = false){

    val nextStep = availableSteps.poll()

    if (isDebug) {
        println("Assigning step: $nextStep")
    }

    val nextWorker = workerQueue.poll()
    workerQueue.add(WorkItem(nextStep, timeToProcess(nextStep, timeDelay)))

    if (isDebug) {
        println("Worker assigned: $nextWorker")
    }
}

private fun getInstructions(lines: MutableList<String>, isDebug : Boolean = false): MutableMap<String, MutableList<String>>{
    val instructions = mutableMapOf<String, MutableList<String>>()
    val nextSteps = PriorityQueue<String>()

    // Fill instructions
    for (line in lines) {
        val matchResult = REGEX.find(line)!!
        val (step1, step2) = matchResult.destructured

        if (!nextSteps.contains(step1)) {
            nextSteps.add(step1)
        }

        if (step2 in instructions.keys) {
            instructions[step2]?.add(step1)
        } else {
            instructions[step2] = mutableListOf(step1)
        }
    }

    // Add steps without dependencies
    for (step in nextSteps) {
        if (step !in instructions.keys) {
            instructions[step] = mutableListOf()
        }
    }

    return instructions
}