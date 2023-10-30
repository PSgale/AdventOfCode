// #1 @ 1,3: 4x4
private val REGEX = Regex("^#(\\d+)\\s@\\s(\\d+),(\\d+):\\s(\\d+)x(\\d+)\$")

fun main() {
    val inputs = "src/main/inputs/"
    var notOverlappedClaimId = 0

    notOverlappedClaimId = getClaimedInchesG1(inputs + "03-claimed_inches-t1.txt", true)
    println("rez: $notOverlappedClaimId")

    notOverlappedClaimId = getClaimedInchesG1(inputs + "03-claimed_inches-p1.txt")
    println("rez: $notOverlappedClaimId")
}

private fun getClaimedInchesG1(it: String, isDebug: Boolean = false): Int {
    val lines = readFileLines(it)

    // fabric[i][j] = how many times this inch was claimed
    val fabric: Array<Array<Int>> = Array(1000) { Array(1000) { 0 } }

    for (line in lines) {
        val (id, offsetLeft, offsetTop, width, height) = parseLine(line)

        if (isDebug)
            println("Parsed: offsetLeft = $offsetLeft, offsetTop = $offsetTop, width = $width, height = $height")

        for (i in offsetLeft until offsetLeft + width) {
            for (j in offsetTop until  offsetTop + height) {
                fabric[i][j] += 1
            }
        }
    }

    var SumOfClaims = 0
    for (line in lines) {
        val (id, offsetLeft, offsetTop, width, height) = parseLine(line)

        SumOfClaims = getSumOfClaims(fabric, offsetLeft, offsetTop, width, height)
        if (SumOfClaims == width * height)
            return id
    }

    return -1
}

private fun getSumOfClaims(fabric:Array<Array<Int>>, offsetLeft: Int, offsetTop: Int, width: Int, height: Int): Int {
    var SumOfClaims = 0

    for (i in offsetLeft until offsetLeft + width) {
        for (j in offsetTop until  offsetTop + height) {

            // collision found
            if (fabric[i][j] > 1)
                return -1

            SumOfClaims += fabric[i][j]
        }
    }

    return SumOfClaims
}

private fun parseLine(line: String): IntArray {
    val matchResult = REGEX.find(line)!!
    val (id, offsetLeft, offsetTop, width, height) = matchResult.destructured
    return intArrayOf(id.toInt(), offsetLeft.toInt(), offsetTop.toInt(), width.toInt(), height.toInt())
}