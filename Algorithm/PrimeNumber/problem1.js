/*
  소수 만들기 (프로그래머스 Summer/Winter Coding ~2018)
  주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하라
*/

const primeCheck = (n) => {
  for (let i = 0; i <= Math.sqrt(n); i++) {
    if (n % i == 0) return false;
  }
  return true;
};

function solution(nums) {
  let cnt = 0;

  for (let i = 0; i < nums.length - 2; i++) {
    for (let j = i + 1; j < nums.length - 1; j++) {
      for (let k = j + 1; k < nums.length - 2; k++) {
        console.log(nums[i] + "/" + nums[j] + "/" + nums[k]);
        if (primeCheck(nums[i] + nums[j] + nums[k])) {
          cnt++;
        }
      }
    }
  }
  return cnt;
}
