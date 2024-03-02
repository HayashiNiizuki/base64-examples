using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;


namespace CSharp_WPF
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void DecodeButton_Click(object sender, RoutedEventArgs e)
        {
            String Text = Base64Box.Text.Trim();
            Byte[] Bytes = Convert.FromBase64String(Text);
            SourceBox.Text = Encoding.UTF8.GetString(Bytes);
        }

        private void EncodeButton_Click(object sender, RoutedEventArgs e)
        {
            String Text = SourceBox.Text.Trim();
            Byte[] Bytes = Encoding.UTF8.GetBytes(Text);
            Base64Box.Text = Convert.ToBase64String(Bytes);
        }
    }
}