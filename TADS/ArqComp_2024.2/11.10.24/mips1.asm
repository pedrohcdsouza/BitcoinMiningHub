.text
main: addi $8, $0, 7 # <= $0 + 7 OBS: ADDI soma um valor, ADD soma uma variavel
      addi $9, $0, 5 # <= $0 + 5
      add $10, $8, $9 # $10 <= $8 + $9
      sub $11, $8, $9 # $11 <= $8 - $9
      
      mul $12, $8, $9 # $12 <= $8 * $9
      div $8, $9 # Hi = $8 % $9
      		 # Lo = $8 // $9
      		 