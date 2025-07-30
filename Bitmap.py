import sys

bitmap = """....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print('Bitmap Message by Samuel Grant')
print('Enter the message to display with the bitmap:')
message = input('> ')
if message == '':
    sys.exit() # Won't execute anything

# Loop over each character in the line
for line in bitmap.splitlines():
    # Loop over each character in a line
    for j, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's a space in bitmap
            print(' ', end='')
        else:
            # Print a character from the message
            print(message[j % len(message)], end='')
    print()