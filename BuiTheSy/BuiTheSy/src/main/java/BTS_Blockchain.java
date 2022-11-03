import java.security.Security;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class BTS_Blockchain {
    public static ArrayList<VNPT_Sy> blockchain = new ArrayList<VNPT_Sy>();
    public static HashMap<String,TransactionOutput> UTXOs = new HashMap<String,TransactionOutput>();

    public static int difficulty = 3;
    public static float minimumTransaction = 0.1f;
    public static Store store1; //Kho 1
    public static Store store2; //Kho 2
    public static Transaction genesisTransaction;

    public static void main(String[] args) {
        //add our blocks to the blockchain ArrayList:
        Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider()); //Thiết lập bảo mật bằng phương thức BouncyCastleProvider

        //Create stores:
        store1 = new Store();
        store2 = new Store();
        Store coinbase = new Store();

        //Khởi tạo giao dịch gốc, nhập từ bàn phím số lượng điện thoại đến kho 1, kho 2
        Scanner BlockData = new Scanner(System.in);

        System.out.println("Hãy nhập số lượng điện thoại của kho 1: ");
        int i = Integer.parseInt(BlockData.nextLine());
        genesisTransaction = new Transaction(coinbase.publicKey, store1.publicKey, i, null);
        genesisTransaction.generateSignature(coinbase.privateKey);	 //Gán private key (ký thủ công) vào giao dịch gốc
        genesisTransaction.transactionId = "0"; //Gán ID cho giao dịch gốc
        genesisTransaction.outputs.add(new TransactionOutput(genesisTransaction.reciepient, genesisTransaction.value, genesisTransaction.transactionId)); //Thêm Transactions Output
        UTXOs.put(genesisTransaction.outputs.get(0).id, genesisTransaction.outputs.get(0)); //Lưu giao dịch đầu tiên vào danh sách UTXOs.

        System.out.println("Hãy nhập số lượng điện thoại của kho 2: ");
        int j = Integer.parseInt(BlockData.nextLine());
        Transaction genesisTransaction2 = new Transaction(coinbase.publicKey, store2.publicKey, j, null);
        genesisTransaction2.generateSignature(coinbase.privateKey);	 //Gán private key (ký thủ công) vào giao dịch gốc
        genesisTransaction2.transactionId = "0"; //Gán ID cho giao dịch gốc
        genesisTransaction2.outputs.add(new TransactionOutput(genesisTransaction2.reciepient, genesisTransaction2.value, genesisTransaction2.transactionId)); //Thêm Transactions Output
        UTXOs.put(genesisTransaction2.outputs.get(0).id, genesisTransaction2.outputs.get(0)); //Lưu giao dịch đầu tiên vào danh sách UTXOs.

        System.out.println("Đang tạo và đào khối gốc .... ");
        VNPT_Sy genesis = new VNPT_Sy("0");
        genesis.addTransaction(genesisTransaction);
        genesis.addTransaction(genesisTransaction2);
        addBlock(genesis);

        System.out.println("\nSố lượng điện thoại trong kho 1: " + store1.getBalance());
        System.out.println("\nSố lượng điện thoại trong kho 2: " + store2.getBalance());

        //Thử nghiệm
        System.out.println("\nNhập số lượng điện thoại cần chuyển từ kho 1 đến kho 2:");
        int k = Integer.parseInt(BlockData.nextLine());
        do {
            VNPT_Sy block1 = blockchain.get(blockchain.size()-1);
            //VNPT_BTS block1 = new VNPT_BTS(genesis.hash);
            VNPT_Sy block2 = new VNPT_Sy(block1.hash);
            block2.addTransaction(store1.sendFunds(store2.publicKey, k));
            addBlock(block2);
            System.out.println("\nNhập số lượng điện thoại cần chuyển từ kho 1 đến kho 2:");
            k = Integer.parseInt(BlockData.nextLine());
        } while (k>i);

        VNPT_Sy block1 = blockchain.get(blockchain.size()-1);
        //VNPT_Sy block1 = new VNPT_Sy(genesis.hash);
        VNPT_Sy block2 = new VNPT_Sy(block1.hash);
        block2.addTransaction(store1.sendFunds(store2.publicKey, k));
        addBlock(block2);
        System.out.println("\nSố lượng điện thoại mới trong kho 1: " + store1.getBalance());
        System.out.println("\nSố lượng điện thoại mới trong kho 2: " + store2.getBalance());

        isChainValid();
    }

    public static Boolean isChainValid() {
        VNPT_Sy currentBlock;
        VNPT_Sy previousBlock;
        String hashTarget = new String(new char[difficulty]).replace('\0', '0');
        HashMap<String,TransactionOutput> tempUTXOs = new HashMap<String,TransactionOutput>(); //Tạo một danh sách hoạt động tạm thời của các giao dịch chưa được thực thi tại một trạng thái khối nhất định.
        tempUTXOs.put(genesisTransaction.outputs.get(0).id, genesisTransaction.outputs.get(0));

        //loop through blockchain to check hashes:
        for(int i=1; i < blockchain.size(); i++) {

            currentBlock = blockchain.get(i);
            previousBlock = blockchain.get(i-1);
            //Kiểm tra, so sánh mã băm đã đăng ký với mã băm được tính toán
            if(!currentBlock.hash.equals(currentBlock.calculateHash()) ){
                System.out.println("#Mã băm khối hiện tại không khớp");
                return false;
            }
            //So sánh mã băm của khối trước với mã băm của khối trước đã được đăng ký
            if(!previousBlock.hash.equals(currentBlock.previousHash) ) {
                System.out.println("#Mã băm khối trước không khớp");
                return false;
            }
            //Kiểm tra xem mã băm có lỗi không
            if(!currentBlock.hash.substring( 0, difficulty).equals(hashTarget)) {
                System.out.println("#Khối này không đào được do lỗi!");
                return false;
            }

            //Vòng lặp kiểm tra các giao dịch
            TransactionOutput tempOutput;
            for(int t=0; t <currentBlock.transactions.size(); t++) {
                Transaction currentTransaction = currentBlock.transactions.get(t);

                if(!currentTransaction.verifySignature()) {
                    System.out.println("#Chữ ký số của giao dịch (" + t + ") không hợp lệ");
                    return false;
                }
                if(currentTransaction.getInputsValue() != currentTransaction.getOutputsValue()) {
                    System.out.println("#Các đầu vào không khớp với đầu ra trong giao dịch (" + t + ")");
                    return false;
                }

                for(TransactionInput input: currentTransaction.inputs) {
                    tempOutput = tempUTXOs.get(input.transactionOutputId);

                    if(tempOutput == null) {
                        System.out.println("#Các đầu vào tham chiếu trong giao dịch (" + t + ") bị thiếu!");
                        return false;
                    }

                    if(input.UTXO.value != tempOutput.value) {
                        System.out.println("#Các đầu vào tham chiếu trong giao dịch (" + t + ") có giá trị không hợp lệ");
                        return false;
                    }

                    tempUTXOs.remove(input.transactionOutputId);
                }

                for(TransactionOutput output: currentTransaction.outputs) {
                    tempUTXOs.put(output.id, output);
                }

                if( currentTransaction.outputs.get(0).reciepient != currentTransaction.reciepient) {
                    System.out.println("#Giao dịch(" + t + ") có người nhận không đúng!");
                    return false;
                }
                if( currentTransaction.outputs.get(1).reciepient != currentTransaction.sender) {
                    System.out.println("#Đầu ra của giao (" + t + ") không đúng với người gửi.");
                    return false;
                }

            }

        }
        System.out.println("Chuỗi khối hợp lệ!");
        return true;
    }

    public static void addBlock(VNPT_Sy newBlock) {
        newBlock.mineBlock(difficulty);
        blockchain.add(newBlock);
    }
}
