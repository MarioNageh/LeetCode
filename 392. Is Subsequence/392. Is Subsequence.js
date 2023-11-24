/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

var isSubsequence = function (s, t) {
    if (s.length > t.length) return false;
    if (s === "") return true // Empty String Is Valid SubSequence
    let i = 0; // For S
    let j = 0 // For J
    while (i < s.length && j < t.length) {
        if (s[i] === t[j]) i++;

        j++
    }
    return i === s.length;


};