import SwiftUI

struct ContentView: View {
    @StateObject private var viewModel = FunctionCallingViewModel()

    var body: some View {
        VStack {
            List(viewModel.messages) { message in
                Text(message.message)
            }

            if viewModel.busy {
                ProgressView()
            } else {
                Button("Speak") {
                    viewModel.startRecognition()
                }
                .padding()
            }
        }
        .onChange(of: viewModel.recognizedText) { newText in
            if !newText.isEmpty {
                Task {
                    await viewModel.sendMessage(newText)
                }
            }
        }
        .alert(isPresented: $viewModel.hasError) {
            Alert(title: Text("Error"), message: Text(viewModel.error?.localizedDescription ?? "Unknown error"), dismissButton: .default(Text("OK")))
        }
    }
}