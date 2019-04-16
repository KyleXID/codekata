//Day2 정수인 숫자를 인자로 받아. 그 숫자를 뒤집어서 return 하는 함수
function reverse(x) {
  x=x.toString();
  let re = [];
  for(let i =0 ; i<x.length; i++) {
	  re[i] = x.slice(i,i+1);
  }	

  let re1 = [];   
  let x1 = 0;
  if ( re[0] === '-') {
	  for(let i=1; i<re.length; i++) {
		  re1[0] = '-';
		  re1[i] = re[re.length-i];
		  x1 =  x1 + re1[i];
	  }return -Number(x1);
  } else {
	  for(let i=0; i<re.length; i++) {
		  re1[i] = re[re.length-1-i];
		  x1 = x1 + re1[i];
	  }return Number(x1);
  }				    
}

console.log(reverse(-87210));
