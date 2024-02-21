function isAnagram(s: string, t: string): boolean {

   function checkFrequency(str: string){
    let map = new Map<string, number>()
    for(let char of str){
        map.set(char, (map.get(char) || 0) + 1)
    }
    return map
   }

   const anogram_s = checkFrequency(s)
   const anogram_t = checkFrequency(t)

   if(anogram_s.size !== anogram_t.size){
    return false
   }
   for(const [char, count] of anogram_s){
    if(anogram_t.get(char) !== count){
        return false
    }
   }

return true
   
};