import scala.collection.mutable.HashMap 


object Hello {
    def main(args: Array[String]): Unit = {
       var hashMap = HashMap("0"->0, "1"->1, "2"->2,"3"->3,"4"->4,"5"->5,"6"->6,"7"->7, "8"->8,"9"->9,"A"->10,"B"->11,"C"->12,"D"->13,"E"->14,"F"->15)  

        var value: String = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        for (a <- 0 until value.length() by 2){
          var stringValue: String = value.slice(a,a+2)
          var intValue: Double = 0
          var base : Double = 16.0
          intValue = intValue + hashMap(value.slice(a,a+1).capitalize) * Math.pow(base,1.0)
          intValue = intValue + hashMap(value.slice(a+1,a+2).capitalize) * Math.pow(base,0.0)
          println(s"intValue: $intValue, stringValue: $stringValue")
        }
    }
}