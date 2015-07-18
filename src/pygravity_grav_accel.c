#include <Python.h>
#include <gmp.h>
#include <mpfr.h>


static PyObject *grav_accel(PyObject *self, PyObject *args) {
	int prec;
	char *mass;
   char *a1;
   char *a2;
   char *a3;
   char *b1;
   char *b2;
   char *b3;
   char e1_out[6];
   char e2_out[6];
   char e3_out[6];
   char out1[200];
   char out2[200];
   char out3[200];
   //clear our output char[]'s or there might be garbage in them
   memset(&e1_out[0], 0, sizeof(e1_out));
   memset(&e2_out[0], 0, sizeof(e2_out));
   memset(&e3_out[0], 0, sizeof(e3_out));
   memset(&out1[0], 0, sizeof(out1));
   memset(&out2[0], 0, sizeof(out2));
   memset(&out3[0], 0, sizeof(out3));
   //mpfr high precision types
   mpfr_t A1, A2, A3, B1, B2, B3, R1, R2, R3, R1q, R2q, R3q, G, R_tmp, Mass;
   
   //store exponent for later output
   mp_exp_t  e1, e2, e3;
   
	//Parse arguments
   if (!PyArg_ParseTuple(args, "isssssss",&prec, &mass, &a1, &a2, &a3, &b1, &b2, &b3)) {
      return NULL;
   }
   
   /*init Rs, R_temp, R_q. These are only initalized, the values come from
    * later computation
    */
   mpfr_init2 (R1, prec);
   mpfr_init2 (R2, prec);
   mpfr_init2 (R3, prec);
   mpfr_init2 (R1q, prec);
   mpfr_init2 (R2q, prec);
   mpfr_init2 (R3q, prec);
   mpfr_init2 (R_tmp, prec);
   
   //set grav constant
   mpfr_init2 (G, prec);
   mpfr_set_str (G, "6.67191e-11", 10, MPFR_RNDD);
   //set mass
   mpfr_init2 (Mass, prec);
   mpfr_set_str (Mass, mass, 10, MPFR_RNDD);
   //init each mpfr_t variable and pass inputted stringss
   	mpfr_init2 (A1, prec);
	mpfr_set_str (A1, a1, 10, MPFR_RNDD);
	
	mpfr_init2 (A2, prec);
	mpfr_set_str (A2, a2, 10, MPFR_RNDD);
	
	mpfr_init2 (A3, prec);
	mpfr_set_str (A3, a3, 10, MPFR_RNDD);
	
	mpfr_init2 (B1, prec);
	mpfr_set_str (B1, b1, 10, MPFR_RNDD);
	
	mpfr_init2 (B2, prec);
	mpfr_set_str (B2, b2, 10, MPFR_RNDD);
	
	mpfr_init2 (B3, prec);
	mpfr_set_str (B3, b3, 10, MPFR_RNDD);
	
	//Find difference vector R between A and B
	mpfr_sub (R1, A1, B1, MPFR_RNDN);
	mpfr_sub (R2, A2, B2, MPFR_RNDD);
	mpfr_sub (R3, A3, B3, MPFR_RNDD);
	
	//find R^2
	mpfr_pow_si (R1q, R1, 2, MPFR_RNDN);
	mpfr_pow_si (R2q, R2, 2, MPFR_RNDN);
	mpfr_pow_si (R3q, R3, 2, MPFR_RNDN);
	
	//Find sum of R1q, R2q, R3q
	mpfr_add (R_tmp, R1q, R2q, MPFR_RNDD);
	mpfr_add (R_tmp, R_tmp, R3q, MPFR_RNDD);
	
	//raise R_temp to 3/2 power
	mpfr_pow_si (R_tmp, R_tmp, 3, MPFR_RNDN);
	mpfr_sqrt (R_tmp, R_tmp, MPFR_RNDN);
	
	/*multiply by G and mass then divide by R_temp
	 * So i don't have to use another mpfr val, I will
	 * divide r_tmp by G, then Mass, then invert
	*/
	mpfr_div (R_tmp, R_tmp, Mass, MPFR_RNDN);
	mpfr_div (R_tmp, R_tmp, G, MPFR_RNDN);
	mpfr_si_div (R_tmp, 1, R_tmp, MPFR_RNDN);
	 
	 //multiply each R by R_temp, which should equal acceleration vector
	 mpfr_mul (A1 , R1, R_tmp, MPFR_RNDN);
	 mpfr_mul (A2 , R2, R_tmp, MPFR_RNDN);
	 mpfr_mul (A3 , R3, R_tmp, MPFR_RNDN);
	 
	//convert A,B,C to string
	a1 = mpfr_get_str(NULL, &e1,10,0, A1,MPFR_RNDN);
	a2 = mpfr_get_str(NULL, &e2,10,0, A2,MPFR_RNDN);
	a3 = mpfr_get_str(NULL, &e3,10,0, A3,MPFR_RNDN);
	
	//Formated new string with exponent and decimal place
	//out1
	
	strncat(out1, &a1[0],1);
	strncat(out1, ".",3);
	int i;
	for(i=1; a1[i] != '\0'; i++){
		strncat(out1, &a1[i],1);
	}
	
	sprintf(e1_out, "e%d",(int)e1);
	strncat(out1, e1_out, 4);
	//out2
	
	strncat(out2, &a2[0],1);
	strncat(out2, ".",3);
	for(i=1; a2[i] != '\0'; i++){
		strncat(out2, &a2[i],1);
	}
	
	sprintf(e2_out, "e%d",(int)e2);
	strncat(out2, e2_out, 4);
	//out3
	
	strncat(out3, &a3[0],1);
	strncat(out3, ".",3);
	for(i=1; a3[i] != '\0'; i++){
		strncat(out3, &a3[i],1);
	}
	
	sprintf(e3_out, "e%d",(int)e3);
	strncat(out3, e3_out, 4);
	 
	 //free mpfr vars
	 mpfr_clear (A1);
	 mpfr_clear (A2);
	 mpfr_clear (A3);
	 mpfr_clear (B1);
	 mpfr_clear (B2);
	 mpfr_clear (B3);
	 mpfr_clear (R1);
	 mpfr_clear (R2);
	 mpfr_clear (R3);
	 mpfr_clear (R1q);
	 mpfr_clear (R2q);
	 mpfr_clear (R3q);
	 mpfr_clear (Mass);
	 mpfr_clear (R_tmp);
	 mpfr_clear (G);
	 
   /* Do something interesting here. */
   return Py_BuildValue("sss", out1,out2,out3);
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
