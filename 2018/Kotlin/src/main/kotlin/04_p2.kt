import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

private val REGEX = Regex("^\\[(.+)]\\s(.+)\$")
private val GUARD = Regex("Guard #(?<guardId>\\d+) begins shift")

private val pattern = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm")

fun main() {
    val inputs = "src/main/inputs/"
    var currentGuard: Guard? = null

    currentGuard = getSleepyGuard(inputs + "04-duty_records-t1.txt", true)
    println("Guard ${currentGuard.id} spent minute ${currentGuard.minuteMostAsleep()} asleep more than any other guard or minute. Answer: ${currentGuard.id * currentGuard.minuteMostAsleep()}")

    currentGuard = getSleepyGuard(inputs + "04-duty_records-p1.txt")
    println("Guard ${currentGuard.id} spent minute ${currentGuard.minuteMostAsleep()} asleep more than any other guard or minute. Answer: ${currentGuard.id * currentGuard.minuteMostAsleep()}")
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

    // Found Guard which spent minute asleep more than any other guard or minute.
    val sortedGuards = guards.values.sortedWith(compareBy { -it.maxTimesAsleepAtSameMinute() })
    return sortedGuards[0]
}