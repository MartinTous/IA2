/* Sistema experto para mantenimiento de sistema de control de valvula de seguridad en estacion de reduccion de presion de gas */

/* Axiomas (invariantes del dominio) */

/* RAMA CENTRAL DEL ARBOL*/
check(piloto) :- 
                condition(piloto, yes), writeln('Set the safety valve according to the instructions').

check(piloto) :- 
                condition(piloto, desconocido), 
                ((condition(leakage_prevention_between_sit_and_orifice, yes), writeln('Pilot full service and reinstallation'));
                check(leakage_prevention_between_sit_and_orifice)).

check(leakage_prevention_between_sit_and_orifice) :- 
                condition(leakage_prevention_between_sit_and_orifice, desconocido), 
                ((condition(safety_valve_spring, yes), writeln('Replace sit and put the safety valve into circuit')); 
                check(safety_valve_spring)).

check(safety_valve_spring) :- 
                condition(safety_valve_spring, desconocido), 
                ((condition(control_valve_sensors_blocked, no), writeln('Putting spring and safety in the service')); 
                check(control_valve_sensors_blocked)).

check(control_valve_sensors_blocked) :- 
                condition(control_valve_sensors_blocked, desconocido), 
                ((condition(valve_status_closed, no), writeln('Cleaning and troubleshooting of the sensing pipes')); 
                check(valve_status_closed)).
                
check(valve_status_closed) :- 
                condition(valve_status_closed, desconocido),
                ((condition(relief_valve_ok_with_10_percent_more_pressure, no), writeln('Place the safety valve in open position'));
                check(relief_valve_ok_with_10_percent_more_pressure)).
                
check(relief_valve_ok_with_10_percent_more_pressure) :- 
                condition(relief_valve_ok_with_10_percent_more_pressure, desconocido),
                ((condition(safety_valve_has_continuous_evacuation, no), writeln('Safety function is appropiate')); 
                check(safety_valve_has_continuous_evacuation)).



check(fuga_preventiva) :- 
                condition(fuga_preventiva, yes), writeln('Set the safey valve according to the instructions').

check(fuga_preventiva) :- 
                condition(fuga_preventiva, desconocido), 
                ((condition(safety_spring, yes), writeln('Replace sit and put the safety valve into circuit'));
                check(safety_spring)).

check(safety_spring) :-
                condition(safety_spring, desconocido), 
                ((condition(control_and_pressure_sensce_pipes_blocked, yes), writeln('Replace the safety spring in the service')); 
                check(control_and_pressure_sensce_pipes_blocked)).

check(control_and_pressure_sensce_pipes_blocked) :-
                condition(control_and_pressure_sensce_pipes_blocked, desconocido), 
                ((condition(line_gas_pressure, no), writeln('Clean up and fix the faults of the sensig pipes')); 
                check(line_gas_pressure)).

check(line_gas_pressure) :-
                condition(line_gas_pressure, desconocido), 
                ((condition(safety_valve_has_continuous_evacuation, yes), writeln('Adjust the regulator according to the instructions')); 
                check(safety_valve_has_continuous_evacuation)).



check(safety_valve_has_continuous_evacuation) :- 
                condition(safety_valve_has_continuous_evacuation, desconocido), 
                writeln('check safety valve has continuous evacuation').


/* RAMA IZQUIERDA DEL ARBOL*/

/* RAMA DERECHA DEL ARBOL*/

/* Ground Facts de instancia variables (podrian resolverse mediante sensado o agregando la informacion interactivamente a la base de conocimientos) */

/* RAMA CENTRAL DEL ARBOL*/
condition(piloto, desconocido).
condition(leakage_prevention_between_sit_and_orifice, desconocido).
condition(safety_valve_spring, desconocido).
condition(control_valve_sensors_blocked, no).
condition(valve_status_closed, desconocido).
condition(relief_valve_ok_with_10_percent_more_pressure, desconocido).

condition(fuga_preventiva, desconocido).
condition(safety_spring, desconocido).
condition(control_and_pressure_sensce_pipes_blocked,desconocido).
condition(line_gas_pressure,desconocido).

condition(safety_valve_has_continuous_evacuation, desconocido).

/* RAMA IZQUIERDA DEL ARBOL*/
condition(thickness_less_than_the_threshold_limit, desconocido).
condition(parts_effects_of_dazzling_and_rusting, desconocido).

/* RAMA DERECHA DEL ARBOL*/
condition(leakage_fixed_with_wrench, desconocido).
condition(gas_leakage_at_joint, desconocido).