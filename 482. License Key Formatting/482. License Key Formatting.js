/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var licenseKeyFormatting = function(s, k) {
    let stringWithDash = s.replace(/-/g, '').toUpperCase();
    let firstGroupLength = stringWithDash.length % k || k;

   let result = stringWithDash.slice(0,firstGroupLength);
   for (let i = firstGroupLength; i < stringWithDash.length; i += k) {
       result += '-' + stringWithDash.slice(i, i + k);
   }
   return result;
};

console.log(licenseKeyFormatting("5F3Z-2e-9-w", 4)); // "5F3Z-2E9W"
console.log(licenseKeyFormatting("2-5g-3-J", 2)); // "2-5G-3J"
console.log(licenseKeyFormatting("--a-a-a-a-a-", 2)); // "AA-AA"