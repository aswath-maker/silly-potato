define i32 @add(i32 %0, i32 %1) {
entry:
  %2 = add i32 %0, %1
  ret i32 %2
}

define i32 @main() {
entry:
  %r = call i32 @add(i32 3, i32 4)
  ret i32 %r
}