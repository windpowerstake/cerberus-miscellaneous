# cerberus-testnet

# inferno-2
Version of cerberus: v2.0.0

chain-id=inferno-2

[config.toml]
persistent_peers = "ad2d97b4e852c9b1cced5dc5981ffffdefa9d5f1@116.202.143.90:26656"


#timeout_commit: Please set it up to 29s. I took spare machines with small disks at the moment. We can accelerate later on when we are all onboarded and ready for the votings. 

timeout_commit = "29s"

## instructions for old validators of inferno-1, so you can re-use your node


```
sudo systemctl stop cerberusd
cd ~
rm .cerberus/config/addrbook.json
rm .cerberus/config/genesis.json
rm -rf cerberus
git clone https://github.com/cerberus-zone/cerberus
cd cerberus
git checkout v2.0.0
make install
cerberusd tendermint unsafe-reset-all
```


Make sure your version is ok:

```cerberusd version```


Must return v2.0.0


```
peers="ad2d97b4e852c9b1cced5dc5981ffffdefa9d5f1@116.202.143.90:26656"
sed -i.bak -e "s/^persistent_peers *=.*/persistent_peers = \"$peers\"/" ~/.cerberus/config/config.toml
```


Make sure the persistent peer is: `ad2d97b4e852c9b1cced5dc5981ffffdefa9d5f1@116.202.143.90:26656`

Get your genesis.json file from discord or from here: https://github.com/windpowerstake/cerberus-testnet/blob/main/genesis.json

Or just with the command:

```
rm ~/.cerberus/config/genesis.json
wget https://raw.githubusercontent.com/windpowerstake/cerberus-testnet/main/genesis.json -P ~/.cerberus/config/
```


# OLD inferno-1 (do not use, just for the record)
Version of cerberus: v1.0.1

Chain-id=inferno-1

[config.toml]
persistent_peers = "02f22ebf0b5c35f2b3004d3e0c2f40c861950b38@65.109.28.219:38656,898586556c71e1a8843dfb8986e65bb0687bb8df@116.202.143.94:21156"


#timeout_commit: Please set it up to 29s. I took spare machines with small disks at the moment. We can accelerate later on when we are all onboarded and ready for the votings. 

timeout_commit = "29s"


