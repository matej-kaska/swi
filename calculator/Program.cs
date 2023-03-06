using System.Data;
class Program {         
        static void Main(string[] args)
        {
            System.Console.WriteLine("X-Calculator!");
            System.Console.WriteLine("h: Historie");
            System.Console.WriteLine("s: Po výpočtu můžete uložit výsledek do paměti");
            System.Console.WriteLine("r: Resetování paměti");
            System.Console.WriteLine("m: Použijete pamět pro výpočet");
            Display display = new Display();
            Calculator calculator = new Calculator();
            Memory memory = new Memory();
            while(true){
                Process(display, calculator, memory);
                display.text = "";
                System.Console.WriteLine("");
            }
        }

        public static void Process(Display display, Calculator calculator, Memory memory){
            while (true){
                ConsoleKeyInfo x = Console.ReadKey(true);
                if (x.Key == ConsoleKey.Enter) {
                    string? xx = calculator.Compute(display.Show(true));
                    System.Console.Write("=" + xx);
                    x = Console.ReadKey(true);
                    if (x.KeyChar.ToString() == "s") {
                        memory.memory = float.Parse(xx);
                    }
                    break;
                }
                if (x.KeyChar.ToString() == "h"){
                    System.Console.WriteLine("Historie: ");
                    foreach (string line in calculator.history){
                        System.Console.WriteLine(line);
                    }
                }
                else if (x.KeyChar.ToString() == "r"){
                    memory.memory = 0;
                }
                else if (x.KeyChar.ToString() == "m"){
                    display.Add(memory.memory.ToString());
                    display.Show(false);
                }
                else {
                    display.Add(x.KeyChar.ToString());
                    display.Show(false);
                }
            }
            
        }
    }

class Calculator {
    public List<string> history = new List<string>();
    public DataTable dt = new DataTable();

    public string? Compute(string? x){
        string xx = dt.Compute(x, null).ToString();
        this.history.Add(x + "=" + xx);
        return xx;
    }
}

class Display {
    public int cursor;
    public string? text;

    public Display() {
        this.text = "";
    }

    public string Show(bool end) {
        if (end != true){
            System.Console.WriteLine(this.text);
        }
        else {
            System.Console.Write(this.text);
        }
        
        return this.text;
    }

    public void Delete() {
        if (this.text != ""){
            this.text = this.text.Substring(cursor,1);
        }
    }
    public void Add(string x) {
        this.text = this.text + x;
    }
    
}

class Memory {
    public float memory = 0;

    public void SaveMemory(float x){
        this.memory = x;
    }
    public float ReadMemory(){
        return this.memory;
    }
    public void ResetMemory(){
        this.memory = 0;
    }
}