var http=require('http');
var uc=require('upper-case');

http.createServer(function(req,res){
	
	res.writeHead(200,{'content-Type':'text\html'});
	res.write(uc.upperCase("Pramod  Ganjave"));
	res.end();
}).listen(8585)


#install upper-case
#npm install upper-case