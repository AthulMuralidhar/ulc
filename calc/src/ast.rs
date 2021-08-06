use std::fmt;

#[derive(Debug, Copy, Clone, PartialEq, Eq)]
pub enum Operator {
    Plus,
    Minus
}

impl  fmt::Display for Operator {
    // custom display for Operator
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match &self {
            Operator::Plus => write!(f, "+"),
            Operator::Minus => write!(f, "-"),
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum Node {
    Int(i32),
    UnaryExpression {
        op: Operator,
        child: Box<Node>
    },
    BinaryExpression {
        op: Operator,
        lhs: Box<Node>,
        rhs: Box<Node>
    }
}

impl fmt::Display for Node {
    // custom display for Node
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result

    }
}