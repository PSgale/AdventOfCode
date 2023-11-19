import java.util.*

private val REGEX = Regex("Step (.+) must be finished before step (.+) can begin.")

fun main() {
    val inputs = "src/main/inputs/"

    var order = getInstructionsOrder(inputs + "07-instructions_list-t1.txt", true)
    println("Correct order is $order")

    order = getInstructionsOrder(inputs + "07-instructions_list-p1.txt",)
    println("Correct order is $order")
}

private fun getInstructionsOrder(fileName: String, isDebug: Boolean = false): String {
    val lines = readFileLines(fileName)
    val instructions  = getInstructions(lines, isDebug)

    if (isDebug)
        println(instructions)

    val order = getOrder(instructions, isDebug)

    return order
}

private fun getOrder(instructions: MutableMap<String, MutableList<String>>, isDebug : Boolean = false): String{
    val availableSteps = PriorityQueue<String>()
    val visitedSteps = ArrayDeque<String>()
    var order = ""

    // Check instructions without dependencies
    addAvailableStep(instructions, availableSteps, visitedSteps, isDebug)

    // Process instructions in order
    while (availableSteps.size > 0) {
        order += executeInstruction(instructions, availableSteps, isDebug)

        // Check instructions without dependencies
        addAvailableStep(instructions, availableSteps, visitedSteps, isDebug)
    }

    return order
}

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
    availableSteps: PriorityQueue<String>,
    isDebug: Boolean = false): String {

    val nextStep = availableSteps.poll()
    instructions.values.filter { it.contains(nextStep) }.forEach { it.remove(nextStep) }

    if (isDebug) {
        println("Executing step: $nextStep")
    }

    return nextStep
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

data class WorkItem(val name: String?, var time: Int)
