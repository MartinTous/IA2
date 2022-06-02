(define (problem TAC-Transporte)
    (:domain TAC)
    (:objects 
        LA1
        MDZ
        MDQ
        COR
        SAL
        SERVOMOTORES
        TRASDUCTORES
        ACERO4040
    )
    (:init 
        (avion LA1)
        (aeropuerto MDZ)
        (aeropuerto MDQ)
        (aeropuerto COR)
        (aeropuerto SAL)
        (carga SERVOMOTORES)
        (carga TRASDUCTORES)
        (carga ACERO4040)
        (en LA1 MDZ)
        (en SERVOMOTORES MDQ)
        (en TRASDUCTORES MDQ)
        (en ACERO4040 MDQ)
        
    )

    (:goal 
        (and
            (en SERVOMOTORES SAL)
            (en TRASDUCTORES MDZ)
            (en ACERO4040 COR)   
        )
    )


)