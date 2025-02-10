
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { MessageSquare, Users, CreditCard } from "lucide-react";

const Dashboard = () => {
  return (
    <div className="p-8">
      <h1 className="text-2xl font-semibold mb-8">Good Afternoon, Front Office!</h1>
      
      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
        {/* Messages Card */}
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">Total Messages</CardTitle>
            <span className="bg-blue-500 text-white text-xs px-2 py-1 rounded">Current</span>
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold mb-2">3</div>
            <div className="flex items-center space-x-2">
              <div className="text-sm">Successful Messages</div>
              <span className="text-blue-500">100%</span>
            </div>
            <div className="w-full h-2 bg-blue-100 rounded mt-2">
              <div className="h-full bg-blue-500 rounded" style={{ width: "100%" }}></div>
            </div>
          </CardContent>
        </Card>

        {/* Transactions Card */}
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">Total Transactions</CardTitle>
            <span className="bg-green-500 text-white text-xs px-2 py-1 rounded">Current</span>
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold mb-2">21</div>
            <div className="flex items-center space-x-2">
              <div className="text-sm">Successful Transactions</div>
              <span className="text-green-500">52%</span>
            </div>
            <div className="w-full h-2 bg-green-100 rounded mt-2">
              <div className="h-full bg-green-500 rounded" style={{ width: "52%" }}></div>
            </div>
          </CardContent>
        </Card>

        {/* Surveyors Card */}
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">Total Surveyors</CardTitle>
            <span className="bg-yellow-500 text-white text-xs px-2 py-1 rounded">Current</span>
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold mb-2">4</div>
            <div className="flex items-center space-x-2">
              <div className="text-sm">Active Surveyors</div>
              <span className="text-yellow-500">50%</span>
            </div>
            <div className="w-full h-2 bg-yellow-100 rounded mt-2">
              <div className="h-full bg-yellow-500 rounded" style={{ width: "50%" }}></div>
            </div>
          </CardContent>
        </Card>

        {/* Clients Card */}
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">Total Clients</CardTitle>
            <span className="bg-pink-500 text-white text-xs px-2 py-1 rounded">Current</span>
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold mb-2">14</div>
            <div className="flex items-center space-x-2">
              <div className="text-sm">Active Clients</div>
              <span className="text-pink-500">93%</span>
            </div>
            <div className="w-full h-2 bg-pink-100 rounded mt-2">
              <div className="h-full bg-pink-500 rounded" style={{ width: "93%" }}></div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default Dashboard;
