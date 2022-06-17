module fitter_routines
use OMP_LIB
contains
	subroutine sin_fit_brute_force_omp(x, y, n, a, w, p, c, atol, wtol, ptol, ctol, an, wn, pn, cn)
		!Least square sum fit for a*sin(x*w + p) + c
		implicit none
		integer, intent(in) :: n
		real(8), intent(in) :: x(n), y(n)
		real(8), intent(in) :: atol, wtol, ptol, ctol
		integer, intent(in) :: an, wn, pn, cn
		real(8), intent(inout) :: a, w, p, c
		integer :: i, j, k, l
		real(8) :: r(n), best_r, r_tot, a0, w0, p0, c0
		real(8) :: atest, wtest, ptest, ctest, final_best_r, besta, bestw, bestp, bestc

		a0 = a - atol
		w0 = w - wtol
		p0 = p - ptol
		c0 = c - ctol

		best_r = 9999999999.0
		final_best_r = 999999999.9

		!$OMP PARALLEL SHARED(final_best_r, a,w,p,c), &
		!$OMP& PRIVATE(i, j, k, l, besta, bestw, bestp, bestc, atest, wtest, ptest, ctest, best_r, r, r_tot)
		!$OMP DO
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
							besta = atest
							bestw = wtest
							bestp = ptest
							bestc = ctest
						end if 
					end do
				end do
			end do
		end do
		!$OMP END DO
		!$OMP CRITICAL
		if(best_r < final_best_r) then
			final_best_r = best_r
			a = besta
			w = bestw
			p = bestp
			c = bestc
		end if
		!$OMP END CRITICAL
		!$OMP END PARALLEL

	end subroutine sin_fit_brute_force_omp

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
