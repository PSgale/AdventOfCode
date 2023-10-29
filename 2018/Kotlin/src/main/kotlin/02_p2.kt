fun main() {
    val inputs = "src/main/inputs/"
    var commonLetters = ""

    commonLetters = getIDs(inputs + "02-box_ids-t2.txt")
    println("rez: $commonLetters")

    commonLetters = getIDs(inputs + "02-box_ids-p1.txt")
    println("rez: $commonLetters")
}

private fun getIDs(it: String, isDebug: Boolean = false): String {
    val lines = readFileLines(it)

    for (i in 0..< lines.size) {
        for (j in 0..< lines.size) {
            if (i == j)
                continue

            val cost = calcCost(lines[i], lines[j], isDebug)

            // cost reached maximum limit
            if (cost == 2) {
                continue
            }

            if (cost == 1)
            {
                return getCommonSubstring(lines[i], lines[j])
            }
        }
    }

    return ""
}

fun calcCost(lhs : String, rhs : String, isDebug: Boolean = false): Int {
    var cost = 0

    val charArrayL = lhs.toCharArray()
    val charArrayR = rhs.toCharArray()

    // size the same
    for (k in 0..< charArrayL.size)
    {
        if (charArrayL[k] != charArrayR[k])
            cost += 1

        // cost reached maximum limit
        if (cost == 2) {
            if (isDebug)
                println("- Compare strings $lhs vs $rhs. Cost reached maximum limit: 2" )
            break
        }
    }

    return cost
}

fun getCommonSubstring(lhs: String, rhs: String): String {
    var common = ""
    for (i in lhs.indices) {
        if (lhs[i] == rhs[i]) {common += lhs[i]}
    }
    return common
}