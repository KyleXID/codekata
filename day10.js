//Day10.Week2(day5) 그래프의 y축의 값을 가진 height 인자를 배열로 받아 그래프 내부에 물을 담는다고 생각했을때, 물을 담을 수 있는 가장 넓은 면적의 값을 반환하는 함수입니다.
function getMaxArea(height) {
  
  let area = 0;
  let maxarea = 0;
  
  for(let i=0; i<height.length-1; i++) {
    
    for(let j=i+1; j<height.length; j++) {
      
      if(height[i] > height[j]) {
        area = height[j] * (j-i);
      } else if(height[i] < height[j]) {
        area = height[i] * (j-i);
      } else {
        area = height[i] * (j-i);
      }
      console.log('area : ',area);
      maxarea = Math.max(area, maxarea);
      console.log('maxarea : ', maxarea);
    }
  }
  return maxarea;
}

console.log(getMaxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]));
