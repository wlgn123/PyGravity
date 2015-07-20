#include <Python.h>
#include <gmp.h>
#include <mpfr.h>

#define ROUND_MODE MPFR_RNDD

static PyObject *grav_accel(PyObject *self, PyObject *args) {
	int prec;
	char *mass;
   char *a1;
   char *a2;
   char *a3;
   char *b1;
   char *b2;
   char *b3;
   char e1_out[10];
   char e2_out[10];
   char e3_out[10];
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
   mpfr_t A1, A2, A3, B1, B2, B3, R1, R2, R3, R1sqr, R2sqr, R3sqr, 
			R1_unit, R2_unit, R3_unit, G, R_tmp, R_mag, Mass;
   
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
   mpfr_init2 (R1sqr, prec);
   mpfr_init2 (R2sqr, prec);
   mpfr_init2 (R3sqr, prec);
   mpfr_init2 (R1_unit, prec);
   mpfr_init2 (R2_unit, prec);
   mpfr_init2 (R3_unit, prec);
   mpfr_init2 (R_tmp, prec);
   mpfr_init2 (R_mag, prec);
   
   //set grav constant
   mpfr_init2 (G, prec);
   mpfr_set_str (G, "6.67191e-11", 10, ROUND_MODE);
   //set mass
   mpfr_init2 (Mass, prec);
   mpfr_set_str (Mass, mass, 10, ROUND_MODE);
   //init each mpfr_t variable and pass inputted stringss
   	mpfr_init2 (A1, prec);
	mpfr_set_str (A1, a1, 10, ROUND_MODE);
	
	mpfr_init2 (A2, prec);
	mpfr_set_str (A2, a2, 10, ROUND_MODE);
	
	mpfr_init2 (A3, prec);
	mpfr_set_str (A3, a3, 10, ROUND_MODE);
	
	mpfr_init2 (B1, prec);
	mpfr_set_str (B1, b1, 10, ROUND_MODE);
	
	mpfr_init2 (B2, prec);
	mpfr_set_str (B2, b2, 10, ROUND_MODE);
	
	mpfr_init2 (B3, prec);
	mpfr_set_str (B3, b3, 10, ROUND_MODE);
	
	//Find difference vector R between A and B

	mpfr_sub (R1, A1, B1, ROUND_MODE);
	mpfr_sub (R2, A2, B2, ROUND_MODE);
	mpfr_sub (R3, A3, B3, ROUND_MODE);
	

	
	//find R^2
	mpfr_pow_si (R1sqr, R1, 2, ROUND_MODE);
	mpfr_pow_si (R2sqr, R2, 2, ROUND_MODE);
	mpfr_pow_si (R3sqr, R3, 2, ROUND_MODE);
	

	
	/*Find sum of R1sqr, R2sqr, R3sqr and squareroot them
	 * after this step R_mag will equal R magnutude
	 */
	mpfr_add (R_tmp, R1sqr, R2sqr, MPFR_RNDD);
	mpfr_add (R_tmp, R_tmp, R3sqr, MPFR_RNDD);
	mpfr_sqrt (R_mag, R_tmp, ROUND_MODE);
	
	//find R_unit
	mpfr_div (R1_unit, R1, R_mag, ROUND_MODE);
	mpfr_div (R2_unit, R2, R_mag, ROUND_MODE);
	mpfr_div (R3_unit, R3, R_mag, ROUND_MODE);
	
	
	
	/*multiply by G and mass then divide by R_temp
	 * So i don't have to use another mpfr val, I will
	 * divide r_tmp by G, then Mass, then invert
	*/
	mpfr_pow_si (R_tmp, R_mag, 2, ROUND_MODE);
	mpfr_div (R_tmp, Mass, R_tmp, ROUND_MODE);
	mpfr_mul (R_tmp, R_tmp, G, ROUND_MODE);
	//mpfr_si_div (R_tmp, 1, R_tmp, ROUND_MODE);
	 
	 //multiply each R by R_temp, which should equal acceleration vector
	 mpfr_mul (A1 , R1_unit, R_tmp, ROUND_MODE);
	 mpfr_mul (A2 , R2_unit, R_tmp, ROUND_MODE);
	 mpfr_mul (A3 , R3_unit, R_tmp, ROUND_MODE);
	 
	 /* SHAMELESS HACK BECUASE IF B1 IS NEGATIVE, 
	  * mpfr_sub  IS 10X TOO BIG
	  * OR MY MATH IS FUCKED UP SOMEWHERE
	  */
	if(mpfr_cmp_ui(B1,0) < 0){
		mpfr_div_ui(A1, A1, 10, ROUND_MODE);
	}
	if(mpfr_cmp_ui(B2,0) < 0){
		mpfr_div_ui(A2, A2, 10, ROUND_MODE);
	}
	if(mpfr_cmp_ui(B3,0) < 0){
		mpfr_div_ui(A3, A3, 10, ROUND_MODE);
	}
	//convert A,B,C to string
	a1 = mpfr_get_str(NULL, &e1,10,0, A1,ROUND_MODE);
	a2 = mpfr_get_str(NULL, &e2,10,0, A2,ROUND_MODE);
	a3 = mpfr_get_str(NULL, &e3,10,0, A3,ROUND_MODE);
	
	//Formated new string with exponent and decimal place
	//out1
	
	strncat(out1, &a1[0],1);
	strncat(out1, ".",3);
	int i;
	for(i=1; a1[i] != '\0'; i++){
		strncat(out1, &a1[i],1);
	}
	
	sprintf(e1_out, "e%d",(int)e1);
	strncat(out1, e1_out, 6);
	//out2
	
	strncat(out2, &a2[0],1);
	strncat(out2, ".",3);
	for(i=1; a2[i] != '\0'; i++){
		strncat(out2, &a2[i],1);
	}
	
	sprintf(e2_out, "e%d",(int)e2);
	strncat(out2, e2_out, 6);
	//out3
	
	strncat(out3, &a3[0],1);
	strncat(out3, ".",3);
	for(i=1; a3[i] != '\0'; i++){
		strncat(out3, &a3[i],1);
	}
	
	sprintf(e3_out, "e%d",(int)e3);
	strncat(out3, e3_out, 6);
	 
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
	 mpfr_clear (R1sqr);
	 mpfr_clear (R2sqr);
	 mpfr_clear (R3sqr);
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
