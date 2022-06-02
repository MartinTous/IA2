(define (domain capp)
(:requirements :equality :strips)
(:predicates
	(orientacion ?o)
    (orientacion-pieza ?op)
  
)


(:action mod_orientacion
 :parameters ( ?oinicial ?ofinal )
 :precondition
	(and 
        (orientacion-pieza ?oinicial) 
        (orientacion ?oinicial) 
        (orientacion ?ofinal)
    )
 :effect
	(and 
		(orientacion-pieza ?ofinal)
		(not (orientacion-pieza ?oinicial))
	)
)

(:action o_fresado
 :parameters ( ?opieza ?ofeature )
 :precondition
	(and 
        (orientacion-pieza ?oinicial) 
        (orientacion ?oinicial) 
        (orientacion ?ofinal)
    )
 :effect
	(and 
		(orientacion-pieza ?ofinal)
		(not (orientacion-pieza ?oinicial))
	)
)








)