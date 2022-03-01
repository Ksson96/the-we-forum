## Data Storage

### Post Table
| Database Key  	| Type           	| Relationship 	|
|---------------	|----------------	|--------------	|
| post_id       	| Int(Unique)    	| PrimaryKey   	|
| title         	| Char(300)      	|              	|
| author        	| User model     	| ForeignKey   	|
| content       	| TextField      	|              	|
| created_date  	| DateTime       	|              	|
| updated_date  	| DateTime       	|              	|
| category_name 	| Category model 	| ForeignKey   	|
| likes         	| User model     	| ManyToMany   	|

### Comments Table
| Database Key 	| Type       	| Relationship 	|                   	|
|--------------	|------------	|--------------	|-------------------	|
| post       	  | Post model 	| ForeignKey   	| Cascade on delete 	|
| author       	| User model 	| ForeignKey   	| Cascade on delete 	|
| body         	| TextField  	|              	|                   	|
| created_date 	| DateTime   	|              	| auto_now_add True 	|
| updated_date 	| DateTime   	|              	|                   	|
| likes        	| User model 	| ManyToMany   	|                   	|

### Category Table
| Database Key  	| Type             	| Relationship 	|
|---------------	|------------------	|--------------	|
| category_name 	| Char(30)(Unique) 	| PrimaryKey   	|
