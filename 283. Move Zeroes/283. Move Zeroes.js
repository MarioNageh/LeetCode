/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let z = 0;
    for (let i = 0; i < nums.length; i++) {
        if(nums[i] !== 0) {
            nums[z] = nums[i];
            z++;
        }
    }
    for (let i = z; i < nums.length; i++) {
        nums[i] = 0;
    }
};
