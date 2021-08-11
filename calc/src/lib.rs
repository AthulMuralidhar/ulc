pub mod ast;
pub mod compiler;
pub mod parser;

pub use crate::ast::{Node, Operator}
// pub use crate::compiler::inter

pub type Result<T> = anyhow::Result<T>;

pub trait Compile