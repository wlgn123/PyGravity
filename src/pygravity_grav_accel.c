#include <Python.h>
#include <math.h>

#define ROUND_MODE MPFR_RNDZ

static PyObject *grav_accel(PyObject *self, PyObject *args) {


   //DECLARE DOUBLE TYPES
   double A1, A2, A3, B1, B2, B3, R1, R2, R3, R1sqr, R2sqr, R3sqr, 
			R1_unit, R2_unit, R3_unit, R_tmp, R_mag, Mass;
   
   // DECLARE VALUE OF G CONSTANT
   double G = -6.67384e-11;
   
	//Parse arguments
   if (!PyArg_ParseTuple(args, "ddddddd", &Mass, &A1, &A2, &A3, &B1, &B2, &B3)) {
      return NULL;
   }
   
	//Find difference vector R between A and B

	R1 =  A1 - B1;
	R2 =  A2 - B2;
	R3 =  A3 - B3;
	

	
	//find R^2
	R1sqr = R1*R1;
	R2sqr = R2*R2;
	R3sqr = R3*R3;
	

	
	/*Find sum of R1sqr, R2sqr, R3sqr and squareroot them
	 * after this step R_mag will equal R magnutude
	 */
	R_tmp =  R1sqr +  R2sqr+ R3sqr;
	R_mag = sqrt(R_tmp);
	
	//find R_unit
	R1_unit = R1/ R_mag;
	R2_unit = R2/ R_mag;
	R3_unit = R3/ R_mag;
	
	
	
	/*multiply by G and mass then divide by R_temp
	 * So i don't have to use another mpfr val, I will
	 * divide r_tmp by G, then Mass, then invert
	*/
	R_tmp = (Mass*G)/ (R_mag*R_mag);

	 //multiply each R by R_temp, which should equal acceleration vector
	 A1 = R1_unit * R_tmp;
	 A2 = R2_unit * R_tmp;
	 A3 = R3_unit * R_tmp;
	 

   return Py_BuildValue("ddd", A1,A2,A3);
}

static char pygravity_grav_accel[] =
    "pygravity_grav_accel( ): Compute Gravity Acceleration in C!!\n";

static PyMethodDef _funcs[] = {
    
       { "grav_accel", grav_accel, METH_VARARGS, NULL },
    {NULL}
};

void initpygravity_grav_accel(void)
{
    Py_InitModule3("pygravity_grav_accel", _funcs,
                   "pygravity_grav_accel!");
}
