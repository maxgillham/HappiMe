/**
* A basic Hello World function
* @param {string} name Who you're saying hello to
* @returns {string}
*/
var data_set = {'day1':'Happy','day2':'meh'}

module.exports = (callback) => {

  callback(null, data_set);

};
