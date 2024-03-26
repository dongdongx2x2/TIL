// https://school.programmers.co.kr/learn/courses/30/lessons/12939

function solution(s) {
  var answer = "";
  let a = s.split(" ");
  answer += Math.min(...a);
  answer += " ";
  answer += Math.max(...a);
  return answer;
}
