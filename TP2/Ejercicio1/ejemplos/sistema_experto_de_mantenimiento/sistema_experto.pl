/* Sistema experto para mantenimiento de sistema de control de valvula de seguridad en estacion de reduccion de presion de gas */

/* Axiomas (invariantes del dominio) */

/* RAMA CENTRAL DEL ARBOL*/
check(piloto) :- 
                condition(piloto, yes), writeln('Set the safety valve according to the instructions').

check(piloto) :- 
                condition(piloto, unknown), 
                ((condition(leakage_prevention_between_sit_and_orifice, yes), writeln('Pilot full service and reinstallation'));
                check(leakage_prevention_between_sit_and_orifice)).

check(leakage_prevention_between_sit_and_orifice) :- 
                condition(leakage_prevention_between_sit_and_orifice, unknown), 
                ((condition(safety_valve_spring, yes), writeln('Replace sit and put the safety valve into circuit')); 
                check(safety_valve_spring)).

check(safety_valve_spring) :- 
                condition(safety_valve_spring, unknown), 
                ((condition(control_valve_sensors_blocked, no), writeln('Putting spring and safety in the service')); 
                check(control_valve_sensors_blocked)).

check(control_valve_sensors_blocked) :- 
                condition(control_valve_sensors_blocked, unknown), 
                ((condition(valve_status_closed, no), writeln('Cleaning and troubleshooting of the sensing pipes')); 
                check(valve_status_closed)).
                
check(valve_status_closed) :- 
                condition(valve_status_closed, unknown),
                ((condition(relief_valve_ok_with_10_percent_more_pressure, no), writeln('Place the safety valve in open position'));
                check(relief_valve_ok_with_10_percent_more_pressure)).
                
check(relief_valve_ok_with_10_percent_more_pressure) :- 
                condition(relief_valve_ok_with_10_percent_more_pressure, unknown),
                ((condition(safety_valve_has_continuous_evacuation, no), writeln('Safety function is appropiate')); 
                check(safety_valve_has_continuous_evacuation)).



check(fuga_preventiva) :- 
                condition(fuga_preventiva, yes), writeln('Set the safey valve according to the instructions').

check(fuga_preventiva) :- 
                condition(fuga_preventiva, unknown), 
                ((condition(safety_spring, yes), writeln('Replace sit and put the safety valve into circuit'));
                check(safety_spring)).

check(safety_spring) :-
                condition(safety_spring, unknown), 
                ((condition(control_and_pressure_sensce_pipes_blocked, yes), writeln('Replace the safety spring in the service')); 
                check(control_and_pressure_sensce_pipes_blocked)).

check(control_and_pressure_sensce_pipes_blocked) :-
                condition(control_and_pressure_sensce_pipes_blocked, unknown), 
                ((condition(line_gas_pressure, no), writeln('Clean up and fix the faults of the sensig pipes')); 
                check(line_gas_pressure)).

check(line_gas_pressure) :-
                condition(line_gas_pressure, unknown), 
                ((condition(safety_valve_has_continuous_evacuation, yes), writeln('Adjust the regulator according to the instructions')); 
                check(safety_valve_has_continuous_evacuation)).



check(safety_valve_has_continuous_evacuation) :- 
                condition(safety_valve_has_continuous_evacuation, unknown), 
                writeln('check safety valve has continuous evacuation').


/* RAMA IZQUIERDA DEL ARBOL*/
check(thickness_less_than_the_threshold_limit) :-
                condition(thickness_less_than_the_threshold_limit, yes), writeln('equipment status will be reported to the technical inspection unit immediately').

check(thickness_less_than_the_threshold_limit) :- 
                condition(thickness_less_than_the_threshold_limit, unknown), 
                ((condition(parts_effects_of_dazzling_and_rusting, no), writeln('The condition of the equipment is suitable'));
                check(parts_effects_of_dazzling_and_rusting)).

check(parts_effects_of_dazzling_and_rusting) :-  
                (condition(parts_effects_of_dazzling_and_rusting, unknown), 
                writeln('Check if the safety valve body, pipes and joints have effects of dazzling and rusting'));
                (condition(parts_effects_of_dazzling_and_rusting, yes), 
                writeln('Coordination is required in order to render and color the equipment'));

/* RAMA DERECHA DEL ARBOL*/

/* Ground Facts de instancia variables (podrian resolverse mediante sensado o agregando la informacion interactivamente a la base de conocimientos) */

/* RAMA CENTRAL DEL ARBOL*/
condition(piloto, unknown).
condition(leakage_prevention_between_sit_and_orifice, unknown).
condition(safety_valve_spring, unknown).
condition(control_valve_sensors_blocked, no).
condition(valve_status_closed, unknown).
condition(relief_valve_ok_with_10_percent_more_pressure, unknown).

condition(fuga_preventiva, unknown).
condition(safety_spring, unknown).
condition(control_and_pressure_sensce_pipes_blocked,unknown).
condition(line_gas_pressure,unknown).

condition(safety_valve_has_continuous_evacuation, unknown).

/* RAMA IZQUIERDA DEL ARBOL*/
condition(thickness_less_than_the_threshold_limit, unknown).
condition(parts_effects_of_dazzling_and_rusting, unknown).

/* RAMA DERECHA DEL ARBOL*/
condition(leakage_fixed_with_wrench, unknown).
condition(gas_leakage_at_joint, unknown).