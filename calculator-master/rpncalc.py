"""Reverse Polish calculator.

This RPN calculator creates an expression tree from
the input.  It prints the expression in algebraic
notation and then prints the result of evaluating it.
"""

import lex
import expr
import sys
import io
from typing import List

BINOPS = {lex.TokenCat.PLUS : expr.Plus,
           lex.TokenCat.TIMES: expr.Times,
           lex.TokenCat.DIV: expr.Div,
           lex.TokenCat.MINUS:  expr.Minus}

symbols = {"+": expr.Plus, "*": expr.Times, "/": expr.Div, "-":  expr.Minus}

def calc(text: str):
    """Read and evaluate a single line formula."""
    try:
        stack = rpn_parse(text)
    except lex.LexicalError as e:
        print(f"*** Lexical error {e}")
        return
    except IndexError:
        # Stack underflow means the expression was imbalanced
        print(f"*** Imbalanced RPN expression, missing operand at {tok.value}")
        return
    if len(stack) == 0:
        print("(No expression)")
    else:
        """For a balanced expression there will be one Expr object
        on the stack, but if there are more we'll just print
        each of them"""
        for exp in stack:
            print(f"{exp} => {exp.eval()}")


def rpn_calc():
    txt = input("Expression (return to quit):")
    while len(txt.strip()) > 0:
        calc(txt)
        txt = input("Expression (return to quit):")
    print("Bye! Thanks for the meth!")

def rpn_parse(text: str) -> List[expr.Expr]:
    """Parse text in reverse Polish notation
    into a list of expressions (exactly one if
    the expression is balanced).
    Example:
        rpn_parse("5 3 + 4 * 7")
          => [ Times(Plus(IntConst(5), IntConst(3)), IntConst(4)))),
               IntConst(7) ]
    May raise:  IndexError (imbalanced expression), lex.LexicalError.
    """
    equation = []
    stack = []
    equation = text.split(" ")
    for value in equation:
        if value in symbols:
            binop_class = symbols[value]
            right = stack.pop()
            left = stack.pop()
            stack.append(binop_class(left, right))
        elif value == "=":
            right = stack.pop()
            left = stack.pop()
            # Reverse left and right
            stack.append(expr.Assign(right, left))
        elif value == "~":
            left = stack.pop()
            stack.append(expr.Neg(left))
        elif value == "@":
            left = stack.pop()
            stack.append(expr.Abs(left))
        elif value.isnumeric():
            new_val = expr.IntConst(int(value))
            stack.append(new_val)
        else:
            stack.append(expr.Var(value))
    return stack


if __name__ == "__main__":
    """RPN Calculator as main program"""
    rpn_calc()





