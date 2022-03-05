# Roadmap for Open Trade with Categosized Smart Contracts
## Inspiration
Inspiration to innovate [Duino-Coin](https://github.com/revoxhere/duino-coin) -based [smart contracts](https://en.wikipedia.org/wiki/Smart_contract) for real physical products comes of current ongoing Russian war against Ukraina, because innocent people are dying there just now and this can be one way to say to Putin, that he is doing wrong things and we don't accept it and that we want to help Ukraina people. But even if Ukraina-case is very very important for us, if we want keep as human people, one very bad thing can also lead good things. Nothing like this has not even been possible before. If we can make full-version of categorised smart contracts, it is possible to check history of a single product of what components it consists and do they fullfill same category contract, than main product clains to fullfill.

Also with components have just same smart contract history data available of sellers and buyers if they fullfill category rules or not, so real controll to real data of how products are made can be available as component level. Even if component is dismanted from one old product and sold to someone, who installs that component to his/her product, new one or old one, also that components history can be found, when component is sold with it's NFT. So business possibities for this kind NFT-usage seems to be very promising if you are going to save the world or even if your are not going to do it.
 
## Steps
### Block-Chain
### Categosized Smart Contracts
Basic idea is based on Categirized Contracts
#### Category
Category for a componen can be based on conditions with a component has build, traded or owned. One example is Russia ban. This category may be defined for instance so, that componen has not beem nade is Russia, not a company that is owned by any people that are citizens by Russia directly or indirectly, phopin use of bullvans. Example of conditions contract may be, that conditions of the workers fullfill some category difined for instance [ILO C029 - Forced Labour Convention, 1930 (No. 29)](https://www.ilo.org/dyn/normlex/en/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C029). Very popular cateryry is nowdays climate carbon neutral, for instance for [Design Buildings](https://www.designingbuildings.co.uk/wiki/Carbon_neutral_contract). This contract is easy to be extended to any area of the business products.

One caterogory will be of hor deep level information of smart contracts of products producing phases and components customer can get, is it only producers annouincement or does it go higher to the deepest level, where same contracts information can be got also for all services and subcomponents that are used in the product.

### Contract Makers
Basically Contract is one-sided. They are promises to follow those category conttracts rules. Producer companies make those promiseses of their products, components or services. Product consist on many components and services of many companies. Chain goes from component makers to product maker to shops, where customer can buy those products.

In this transfer chain component is always holded by one acror. We can identify two type component holder change dependent of that, is component buyed to not, is ownership changed or not. Those actors have made categorised contracts how they behave with that component. We can iedntify assignment between component, actor and contract.

If we look situation in the shop, customer can find out a product that consista of components and services. Even the shop selling assings a service to a product what it is selling and have nade promises how it works. Customer can find out products all components and services and get information od all vategorized contract made ot not made.

On selling phase customer can choose a produuct by a categorized contract and if product does not fullfil this contracts by some component or service, customer can see what is wrong with that product or simply get a list o other products that fullfill the contract wanted. We can find out that with this logic we have made a system, where customer can choose his/her values and put his/her money to talk how this world should act.

### What this projects will sell?

This projects product will be product sticker that includes a QR-code, which has identification information of a prodeucts. From that customer can check if a product fullfilss smart contracts he/she wants. Lokk car componts, cellular phone boxes aetc. All products have stickers, where are many kind is-information. This Categorized Contracts sticker is one more. With that sticker product makers can get get godwill for their products,  products, because they act responsible.

### Open Trade
Because anyone can check the product or product batch that contains the QR code, trading will become open. We cannot assume that this idea will ever be used in all commerce, but it is possible that it will eventually become mainstream.

### Book Keeping
#### Items identified
We can find out, that all items can have same structure and only it's role differs. Role can be actor or component and those roles we can build company, department of a company, product stat consists of componets, component, customer, group of customer, group of customer groups etc.
##### Smart contract
~ id
~ name
~ description
~ url
 
###### Item
Itemt is iterative with roles, so item can be component be basic component that is a part of a product, component, that is not a part of a product yet, a product that contais components, company or department of company, customer or group of customers
~ id
~ name
~ description
~ role (company, department, component, product, customer, customer group
~ set of items that are assembled to this item, this can be also ownership, if role role is company, customer
~ which items this item is part of
~ set of items this item holds. Valid for company that sells services like transport. Transport can also be a component. Because ownership is not changed ith these kind operatoins, we need onother set than obove one. 
~ which items this item is holded of
~ holder who has physical control to this item now, valid for roles company, department
~ set of smart contract this item fullfills (roles company, company) or what smart contract role customer wan't to be fullfilled.


#### Transactions identified
##### Create, modify delete Item
~ id
~ date
~ transaction type (create, modify, delete )
~ Actor data

##### assign or deassign Item
~ id
~ date
~ actor, item with roles company (department), customer(customer group)
~ transaction type (assign or deassign)
~ item id
~ subiten item
~ holder item id
~ holder subitem id

### Implementation
#### Demo
Maybe demo with python3 is the asiest way
#### Final Implementaion
This should work with smart phones. Maybe jave implementation for clients is needed. Propable we need server side.


### Book keeping
There are many possibilities. We can even use pure files almost for a demo, datata base aor block chain. Maybe this is roadmap. Below is some study points for Duino, because it is chep coin, but maybe studu for it should be with a very low priority.

#### Block-Chain
##### Study Block_Chains
##### Study Duino as Block_Chain
Read-only logging is basic feature of a block-chain, but is Duino a block-chain? If yes, how we con log with Duino? If not, is it possible to wrap Duino-Coin to some block-chain?

Suggstion by bobyblobfish#1566: "... make a duino nft on polygon blockchain, and make an official section on the duinocoin website that lets you buy the nfts with duco, but actually it buys it with polygon by exchanging the duino to polygon through the website. Now we have duino nfts that  are decentralized, and also doesn’t force anyone to directly use anything besides duino to buy it." In this use case we should put "smart contract" on a polygon blockchain to keep consepts clear, because it seems that nft is always asociated to some digital thing, but here we have smart contract, which is digital itself, but it is associated to a flysical thing like a component of a product.

Technical link to [Setting up Metamask for Polygon (Matic Network)](https://medium.com/stakingbits/setting-up-metamask-for-polygon-matic-network-838058f6d844)

Your need wallet and Secret Recovery Phrase. Don't yet know if Duino-Coin Web wallet can be used. In this study I created a new wallet and Secret Recovery Phrase. After creating wallet with a phase, it if I try to add network
- Network Name
- New RPC URL
- Chain ID
- Currency Symbol(Optional)
- Block Explorer URL(Optional)

For Etherium these are
- Network Name 			Ethereum Mainnet
- New RPC URL  			***
- Chain ID				1
- Currency Symbol(Optional)		ETH
- Block Explorer URL(Optional)	https://etherscan.io

For tests can be used for instance
- Localhost 8545
- Ropsten Test Network

To continue study, maybe Ropsten Test Network is best.

- Network Name				Ropsten Test Network
- New RPC URL				***
- Chain ID				3	
- Currency Symbol(Optional) 		ETH
- Block Explorer URL(Optional)	https://ropsten.etherscan.io

Hmm.. this is already included, because I can't add it

Currency can be for istance bitcoin, dollar, but no DUCO.


### Smart Contract
#### Study Smart Contracts
How to deploy smart contract? Youcan use ethereum as example, but ethereus is not cheap main think to study is we can lof with Duino, how we deploy smart contyracts with Duino?

### GPL
#### Study GPL
 Study GPL as a purpose to define Smart Contract same kind as GPL so, that contract maker promises publish all components  he/her has used as a list with Smart Contract -information needed for each.

