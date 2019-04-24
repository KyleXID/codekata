//Day8.Week2(day3) 여러 괄호들로 이루어진 인자를 받아 그것이 유효한 표현인지 true/false로 반환하는  함수
function isValid(s) {
  let matching = {
      '(': ')',
      '[': ']',
      '{': '}'
  };

  let closeArr = [];
  let openArr = [];
  let sArr = s.split('');
  let result = true;

  for (let i = 0; i < sArr.length; i++) {
      let thisStr = sArr[i];
      let closeForOpen = matching[thisStr];
      if (closeForOpen) {
        openArr.push(thisStr);
        closeArr.unshift(closeForOpen);
      } 
      else {
        if (thisStr === closeArr[0]) {
          closeArr.shift();
          openArr.pop();
        } else {
          result = false;
          break;
        }
      }
  }
  
  return result && closeArr.length === 0;
}


//또 다른 방법 from [https://github.com/seongto/] by Seongto
function isValid(s) {
  let str = s.slice();
  let length = s.length;

  for (let i = 0; i < length/2; i++){
    for (let j = 0; j < length-1; j++){
      let fair = str[j]+str[j+1];
      if ( (fair === "()") || (fair === "{}") || (fair === "[]")){
        str= str.replace(str[j], "");
	str= str.replace(str[j], "");
      }
    }  
  }
  
  if (str === "") {
    return true
  } else {
    return false
  }  
}
