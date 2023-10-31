import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

private val REGEX = Regex("^\\[(.+)]\\s(.+)\$")
private val GUARD = Regex("Guard #(?<guardId>\\d+) begins shift")

private val pattern = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm")

fun main() {
    val inputs = "src/main/inputs/"
    var currentGuard: Guard? = null

    currentGuard = getSleepyGuard(inputs + "04-duty_records-t1.txt", true)
    println("Most sleepy guard ${currentGuard.id} has been asleep the most at minute ${currentGuard.minuteMostAsleep()}. Answer: ${currentGuard.id * currentGuard.minuteMostAsleep()}")

    currentGuard = getSleepyGuard(inputs + "04-duty_records-p1.txt")
    println("Most sleepy guard ${currentGuard.id} has been asleep the most at minute ${currentGuard.minuteMostAsleep()}. Answer: ${currentGuard.id * currentGuard.minuteMostAsleep()}")
}

private fun getSleepyGuard(fileName: String, isDebug: Boolean = false): Guard {
    val lines = readFileLines(fileName)

    val guards = mutableMapOf<String, Guard>()
    var currentGuard: Guard? = null

    // order duty records
    val splitLines = mutableListOf<Array<String>>()
    for (line in lines) {
        val matchResult = REGEX.find(line)!!
        val (datetime, msg) = matchResult.destructured
        splitLines.add(arrayOf(datetime, msg))
    }
    val actions = splitLines.sortedWith(compareBy { it[0] })

    // identify guards
    for (a in actions) {
        if (a[1] == "falls asleep") {
            val dateTime = LocalDateTime.parse(a[0], pattern)
            currentGuard!!.fallAsleep(dateTime.minute)

            if (isDebug)
                println("- (${dateTime.minute}) - fallAsleep")
        }
        else if (a[1] == "wakes up") {
            val dateTime = LocalDateTime.parse(a[0], pattern)
            currentGuard!!.wakeUp(dateTime.minute)

            if (isDebug)
                println("- (${dateTime.minute}) - wakeUp at")
        }
        else if (GUARD.matches(a[1])) {
            currentGuard?.endShift()
            val guardId = GUARD.find(a[1])!!.groups["guardId"]!!.value

            if (guards.contains(guardId)) {
                currentGuard = guards[guardId]
            } else {
                currentGuard = Guard(guardId.toInt())
                guards[guardId] = currentGuard
            }

            if (isDebug)
                println("Guard: #$guardId begins shift")
        }
    }
    currentGuard?.endShift()

    // Find most sleepy guard who has been asleep the most at same minute.
    val sortedGuards = guards.values.sortedWith(compareBy { -it.totalSleepMinutes() })
    return sortedGuards[0]
}


class Guard(val id: Int) {
    private var isAwake = true
    private val asleepIntervals = mutableListOf<IntArray>()
    private var currentSleep = IntArray(60) { 0 }
    private var sleepStart = 0

    fun fallAsleep(minute: Int) {
        if (!isAwake) throw Exception("The guard sleeps himself into the Matrix")
        isAwake = false
        sleepStart = if (minute > 0) minute else 0
    }

    fun wakeUp(minute: Int) {
        if (isAwake) throw Exception("The guard can not take the cruelty of this world and wake up again")
        isAwake = true
        for (i in sleepStart until minute) currentSleep[i] = 1
    }

    fun endShift() {
        asleepIntervals.add(currentSleep)
        currentSleep = IntArray(60) { 0 }
    }

    fun totalSleepMinutes(): Int {
        var out = 0
        for (sleep in asleepIntervals) { out += sleep.count { it == 1 } }
        return out
    }

    fun minuteMostAsleep(): Int {
        val timesAsleepAt = IntArray(60) { 0 }
        for (sleep in asleepIntervals) {
            for (i in sleep.indices) { if (sleep[i] == 1) timesAsleepAt[i] += 1 }
        }
        return timesAsleepAt.indexOf(timesAsleepAt.max())
    }

    fun maxTimesAsleepAtSameMinute(): Int {
        val timesAsleepAt = IntArray(60) { 0 }
        for (sleep in asleepIntervals) {
            for (i in sleep.indices) { if (sleep[i] == 1) timesAsleepAt[i] += 1 }
        }
        return timesAsleepAt.max()
    }
}