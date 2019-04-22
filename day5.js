//Day5.단어가 담긴 배열을 입력받고 공통된 시작단어(prefix)를 return 하는 함수
function getPrefix(strs) {
  let newi = strs.length;
  let stop = false;
  
  if (newi === 0) return "";
  
  for (let i=0; i<strs[0].length; i++) {
      
    let fc = strs[0].charAt(i);

    for (let j=1; j<strs.length; j++) {
      if ( strs[j].charAt(i) != fc ) {
        newi = i;
        stop = true;
        break;
      }
    }
    
    if (stop) {
      break;
    }
  }

  return strs[0].slice(0, newi);
}

let strs = ['flower', 'flue', 'fly'];
console.log('result', getPrefix(strs));
