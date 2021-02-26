
const NUMBERS = [93,2,8,87,15,17,45,1,23,78,38,29,99,3,55,64,28,83,74,39,44,27,91,
                 52,67,16,65,82,4,9,93,87,18];


var get_halfway_index = function(length) {
    return Math.round(length / 2)
}


console.assert(get_halfway_index(33) === 17)


var binary_search = function(numbers, search, copy = []) {
    if (copy.length == 0) {
      copy = [...numbers];
    }

    // https://www.javascripttutorial.net/javascript-array-sort/
    numbers.sort(function(a , b){
        if(a > b) return 1;
        if(a < b) return -1;
        return 0;
    });

    halfway_index = get_halfway_index(numbers.length);
    let halfway = numbers[halfway_index];
    console.log("Halfway number is " + halfway);

    if (numbers.length == 0) {
        console.log("didn't find it")
        return -1
    }

    if (halfway == search) {
        let number_index = copy.indexOf(search);
        console.log("found it at " + number_index)
        return number_index;
    } else if (halfway > search) {
        let new_numbers_list_to_search = numbers.slice(0, halfway_index);
        console.log("New numbers list to search:");
        console.log(new_numbers_list_to_search);
        binary_search(new_numbers_list_to_search, search, copy);
    } else if (halfway < search) {
        let new_numbers_list_to_search = numbers.slice(halfway_index + 1);
        console.log("New numbers list to search:");
        console.log(new_numbers_list_to_search);
        binary_search(new_numbers_list_to_search, search, copy);
    }
}

var index = binary_search(NUMBERS, 2)
console.log("the index is " + index)

var index_2 = binary_search(NUMBERS, 999)
console.log("the index is " + index_2)
