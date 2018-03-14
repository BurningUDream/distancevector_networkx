# distancevector_networkx

There are many layers in computer networks, and different layers concern about different issues.  
In network layer, ```forwarding``` and ```routing``` are the two important topics. 
* Forwarding is to move packets from router's input to appropriate router's output. 
* Routing is to determine route taken by packets from source to destination. 

As lots of algorithms have been invented and discussed for routing, I implement one of the algorithm which is called distance vector algorithm with the aid of networkx.

In order to keep it simple, I suppose that all the nodes in this network know the the cost of every other nodes' neighbors. So the issues like convergance time won't be discussed here. 

For the detail of distance vector algorithm, refer to [Distance-vector_routing_protocol](https://en.wikipedia.org/wiki/Distance-vector_routing_protocol)

