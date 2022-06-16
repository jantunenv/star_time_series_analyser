module fitter_routines
contains
	subroutine sin_fit_brute_force(x, y, n, a, w, p, c, atol, wtol, ptol, ctol, an, wn, pn, cn)
		!Least square sum fit for a*sin(x*w + p) + c
		implicit none
		integer, intent(in) :: n
		real(8), intent(in) :: x(n), y(n)
		real(8), intent(in) :: atol, wtol, ptol, ctol
		integer, intent(in) :: an, wn, pn, cn
		real(8), intent(inout) :: a, w, p, c
		integer :: i, j, k, l
		real(8) :: r(n), best_r, r_tot, a0, w0, p0, c0
		real(8) :: atest, wtest, ptest, ctest

		a0 = a - atol
		w0 = w - wtol
		p0 = p - ptol
		c0 = c - ctol

		best_r = 9999999999.0

		do i=1,an
			atest = a0 + i*(2*atol/an)
			do j=1,wn
				wtest = w0 + j*(2*wtol/wn)
				do k=1,pn
					ptest = p0 + k*(2*ptol/pn)
					do l=1,cn
						ctest = c0 + l*(2*ctol/cn)
						r = atest*sin(x*wtest + ptest) + ctest 
						r = r - y
						r = r**2
						r_tot = sum(r)
						if(r_tot < best_r) then
							best_r = r_tot
							a = atest
							w = wtest
							p = ptest
							c = ctest
						end if 
					end do
				end do
			end do
		end do

	end subroutine sin_fit_brute_force
end module fitter_routines
