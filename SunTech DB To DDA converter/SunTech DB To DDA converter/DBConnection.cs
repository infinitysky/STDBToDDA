using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SunTech_DB_To_DDA_converter
{
    class DBConnection{
        public string dbLink { get; private set; }
        public string dbName { get; private set; }
        public string dbUsername { get; private set; }
        public string dbPassword { get; private set; }

        public DBConnection(string dbLinkString, string dbNameString, string dbUsernameString, string dbPasswordString )
        {
            this.dbLink = dbLinkString;
            this.dbName = dbNameString;
            this.dbUsername = dbUsernameString;
            this.dbPassword = dbPasswordString;

        }

       
    }
}
