countprefix = function () {

  var prefixes = [21, 22, 231, 232, 233, 234];
  var count_p = 0;

  for(var i in prefixes){
    var c = db.phones.find({"components.prefix":prefixes[i]}).count();
    count_p += c;
    print("Count prefix " + prefixes[i] + ": " + c);
  }
  print("Total: " + count_p);
  print("Done!");
}
