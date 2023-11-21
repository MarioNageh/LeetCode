/**
 * @param {string[]} logs
 * @return {number}
 */
var minOperations = function(logs) {
    let operations = [];
    for(let op in logs) {
        if(logs[op] === "../") {
            if(operations.length > 0)
                operations.pop();
        } else if(logs[op] === "./") {
        } else {
            operations.push(logs[op]);
        }

    }
    return operations.length;
};


console.log(minOperations(["d1/","d2/","../","d21/","./"])); // 2