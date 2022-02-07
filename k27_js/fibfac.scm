;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname fibfac) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname fibfac) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define fact
  (lambda (n)
    (if (= n 0)
        1
        (* (fact (- n 1)) n)
        )
    )
)


(define fib
  (lambda (n)
    (if (<= n 1)
        n
        (+ (fib (- n 1))  (fib (- n 2))
        )
    )
    )
)

(display (fact 0))
(display (fact 1))
(display (fact 2))
(display (fact 3))

(display (fib 0))
(display (fib 1))
(display (fib 2))
(display (fib 3))