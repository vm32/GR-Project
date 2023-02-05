def check_accident(input_value)
  if input_value > 1
    puts "Accident detected"
  else
    puts "No accident detected"
  end
end

print "Enter a value from the web page: "
input_value = gets.to_f
check_accident(input_value)
