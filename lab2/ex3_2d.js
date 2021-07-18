capicua = function () {

  var display = db.phones.find({},{"_id":0,"display":1});
  var size = display.count();
  var count_c = 0;

  for(var i = 0; i < size; i++){
    n = display[i]["display"].split("-")[1];
    if(n == n.split("").reverse().join("")){    
        print(n);
        count_c++;
    }
  }
  print("Total: " + count_c);
  print("Done!");
}
