
function calc_dot(n, vec1, vec2) result(res)
  implicit none
  integer, intent(in) :: n
  double precision, intent(in) :: vec1(n), vec2(n)
  double precision :: res
  double precision, external :: ddot

  res = ddot(n, vec1, 1, vec2, 1)
end function calc_dot

