# 50002-2D-Adder

Various adder designs for the 50.002 component of the term 4 2D project.

## Running the jsim files

1. Download `jsim.jar` from https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/resources/jsim/.
2. Install JRE from https://www.java.com/en/download/manual.jsp.
3. Go to the folder where `jsim.jar` is saved, and run the command  `java -jar jsim.jar`.
4. Open one of the adder jsim files (e.g. `v3_carry_lookahead_3ns.jsim`).
5. Click on "Gate-level simulation" (5th button from the right).
6. In the new window, click on "Complete checkoff" (green tick button) to verify that the adder passes the test cases.
7. In the original jsim window, look at the bottom for the min observed setup time. The tpd of the adder is `CLK time - min setup time` (CLK time is stated in the name of the respective checkoff file e.g. 3ns, 4ns).

## BC and CNF files
`adder.bc` contains the v3 design (lines 3-359), written in BC script (http://users.ics.aalto.fi/tjunttil/circuits/). It also contains the design of a basic ripple carry adder made with AND, OR and XOR gates (lines 363-553). `bcscript.py` is used to easily generate `adder.bc`.

`adder.bc` is used to create a cnf file (`converted_from_bc.cnf`), to check whether the adder design truly works perfectly. This is achieved by taking the most significant bit from the output of each adder design, put them through an XOR gate, and see if it is possible to get an output of 1 (i.e. the bits are different).

If the assert statement is not satsifiable, it means that there are no possible inputs that can cause the two adder designs to produce different outputs, which in turn means that the v3 adder design is functionally identitical to the basic adder design (which is already known to work correctly).

`converted_from_bc.cnf` can be run in a SAT solver, and the expected output should be UNSAT.
