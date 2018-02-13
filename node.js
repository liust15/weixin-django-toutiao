function countWords (str) {
    var length = 0;
    var strArray = str.split(' ');
    
    for(var i = 0;i < strArray.length;i++)
    {
        length = strArray[i].length > length ? strArray[i].length : length;
    }
    
    return length;
    }
    countWords("Good morning, I love JavaScript.")