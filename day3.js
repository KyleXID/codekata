//Day3 Code Kata String인자를 받아 중복되지 않은 알파벳으로 이루어진 가장 긴 단어의 길이를 반환하는 함수입니다.

function getLengthOfStr(s) {
    let strArr = [];
    let prevStrArr = [];
    
    for (let i = 0; i < s.length; i++) {
      
        let ss = s.slice(i, i+1);
        console.log(' 검사 ss ==> ', ss);
        for (let j = 0; j < strArr.length; j++) {
            if (ss === strArr[j]) {
                
                if (prevStrArr.length < strArr.length) {
                    prevStrArr = strArr.slice();
                }
                
                strArr = strArr.splice(j+1, strArr.length);
                break;
            }
        }
        
        strArr.push(ss);
    }
    
    return Math.max(strArr.length, prevStrArr.length);
}

console.log(getLengthOfStr('taaaytts'));
