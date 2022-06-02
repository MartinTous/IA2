(define (domain TAC)
(:requirements :equality :strips)
	(:predicates
		(en ?a ?b)
		(avion ?a)
    	(carga ?c)
    	(aeropuerto ?a)
	)

  (:action cargar
   :parameters ( ?c ?a ?ap )
   :precondition
     (and (en ?c ?ap) (en ?a ?ap)
        (carga ?c) (avion ?a) (aeropuerto ?ap)
      )
   :effect
     (and 
        (en ?c ?a) 
        (not (en ?c ?ap))
      )
  )
  (:action descargar
   :parameters ( ?a ?c ?ap )
   :precondition
     (and (en ?c ?a) (en ?a ?ap)
        (carga ?c) (avion ?a) (aeropuerto ?ap)
      )
   :effect
     (and 
        (en ?c ?ap) 
        (not (en ?c ?a))
      )
  )
  (:action volar
   :parameters ( ?a ?ap1 ?ap2 )
   :precondition
     (and (en ?a ?ap1) 
        (avion ?a) (aeropuerto ?ap1) (aeropuerto ?ap2)
      )
   :effect
     (and 
        (en ?a ?ap2) 
        (not (en ?a ?ap1))
  	  )
   )
)
